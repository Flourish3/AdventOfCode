#![feature(test)]

extern crate test;

use std::fs::File;
use std::io::prelude::*;

trait ToDec {
    fn to_decimal(&self) -> u32;
}

impl<I> ToDec for I
where
    Self: DoubleEndedIterator,
    I: IntoIterator<Item = u32>,
{
    fn to_decimal(&self) -> u32 {
        let enume = self.rev().enumerate();
        
        enume.fold(0, |acc, item| {
            acc + item.1 * 2_u32.pow(item.0.try_into().unwrap())
        })
    }
}

fn calculate_power_consumption(s: String) -> u32 {
    let total_diags: u32 = s.lines().count().try_into().unwrap();
    let size_diag = s.lines().nth(0).unwrap().len();

    let gamma = s
        .lines()
        .map(|line| {
            line.chars()
                .flat_map(|c| c.to_digit(2))
                .collect::<Vec<u32>>()
        })
        .fold(Vec::from(vec![0; size_diag]), |acc, item| {
            acc.iter()
                .zip(item.iter())
                .map(|(a, b)| a + b)
                .collect::<Vec<u32>>()
        })
        .iter()
        .map(|i| if *i > total_diags / 2 { 1_u32 } else { 0_u32 })
        .to_decimal();
    /* .rev()
    .enumerate()
    .fold(0, |acc, item| {
        acc + item.1 * 2_u32.pow(item.0.try_into().unwrap())
    }); */

    let epsilon = !gamma
        & vec![1; size_diag].iter().enumerate().fold(0, |acc, item| {
            acc + item.1 * 2_u32.pow(item.0.try_into().unwrap())
        });

    println! {"{}", epsilon};
    println! {"{:?}", gamma};
    epsilon * gamma
}

fn filter_bit_criteria(
    codes: &Vec<Vec<u32>>,
    bit: usize,
    crit: fn(u32, u32) -> u32,
) -> Vec<Vec<u32>> {
    let total_diags: u32 = codes.len().try_into().unwrap();
    let size_diag = codes.first().unwrap().len();

    let common = codes
        .iter()
        .fold(Vec::from(vec![0; size_diag]), |acc, item| {
            acc.iter()
                .zip(item.iter())
                .map(|(a, b)| a + b)
                .collect::<Vec<u32>>()
        });
    let filtered = codes
        .iter()
        .filter(|code| code[bit] == crit(total_diags, common[bit]))
        .map(|l| l.to_owned())
        .collect::<Vec<Vec<u32>>>();

    if bit + 1 < size_diag && filtered.len() > 1 {
        filter_bit_criteria(&filtered, bit + 1, crit)
    } else {
        filtered
    }
}

fn calculate_life_support_rating(s: String) -> u32 {
    let codes = s
        .lines()
        .map(|line| {
            line.chars()
                .flat_map(|c| c.to_digit(2))
                .collect::<Vec<u32>>()
        })
        .collect::<Vec<Vec<u32>>>();

    let oxygen_gen_rating = filter_bit_criteria(&codes, 0, |total, ones| {
        if ones as f32 / total as f32 >= 0.5 {
            1
        } else {
            0
        }
    })
    .first()
    .unwrap()
    .iter()
    .rev()
    .enumerate()
    .fold(0, |acc, item| {
        acc + item.1 * 2_u32.pow(item.0.try_into().unwrap())
    });

    let co2_scrubber = filter_bit_criteria(&codes, 0, |total, ones| {
        if ones as f32 / total as f32 >= 0.5 {
            0
        } else {
            1
        }
    })
    .first()
    .unwrap()
    .iter()
    .rev()
    .enumerate()
    .fold(0, |acc, item| {
        acc + item.1 * 2_u32.pow(item.0.try_into().unwrap())
    });

    oxygen_gen_rating * co2_scrubber
}

fn main() {
    let mut contents = String::new();
    File::open("../data/03.txt")
        .expect("File not found")
        .read_to_string(&mut contents)
        .expect("Something went wrong when reading");

    //println!("Part 1: {}", calculate_power_consumption(contents));
    println!("Part 2: {}", calculate_life_support_rating(contents));
}

#[cfg(test)]
mod tests {
    use super::*;
    use test::Bencher;

    #[test]
    fn power_consumption_test() {
        let contents = String::from(
            "00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010",
        );

        assert_eq!(calculate_power_consumption(contents), 198);
    }

    #[test]
    fn life_support_test() {
        let contents = String::from(
            "00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010",
        );

        assert_eq!(calculate_life_support_rating(contents), 230);
    }

    #[bench]
    fn bench_diag(b: &mut Bencher) {}
}
