#![feature(test)]

extern crate test;

use std::fs::File;
use std::io::prelude::*;
use std::iter::successors;

fn fuel(mass: &u32) -> Option<u32> { 
    (mass / 3).checked_sub(2)
}

fn part1(input: &Vec<u32>) -> u32 {
    input
    .into_iter()
    .flat_map(|m| fuel(m))
    .sum()
}

fn part2(input: &Vec<u32>) -> u32 {
    input
    .into_iter()
    .flat_map(|m| successors(fuel(m), fuel).collect::<Vec<_>>())
    .sum()
}

fn main() {
    let mut contents = String::new();
    File::open("../data/input01.txt")
        .expect("File not found")
        .read_to_string(&mut contents)
        .expect("Something went wrong reading the file");
    let input = contents.lines().flat_map(|t| t.parse::<u32>()).collect::<Vec<u32>>();

    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}

#[cfg(test)]
mod tests {
    use super::*;
    use test::{Bencher};

    #[test]
    fn test_p1(){
        assert_eq!(part2(&vec!(12_u32)), 2);
    }

    #[test]
    fn test_p2(){
        assert_eq!(part2(&vec!(100756_u32)), 50346);
    }

    #[bench]
    fn bench_part1(b: &mut Bencher) {
        let mut contents = String::new();
        File::open("../data/input01.txt")
            .expect("File not found")
            .read_to_string(&mut contents)
            .expect("Something went wrong reading the file");
        let input = contents.lines().flat_map(|t| t.parse::<u32>()).collect::<Vec<u32>>();
        
        b.iter(|| {
            part1(&input);
        });
    }

    #[bench]
    fn bench_part2(b: &mut Bencher) {
        let mut contents = String::new();
        File::open("../data/input01.txt")
            .expect("File not found")
            .read_to_string(&mut contents)
            .expect("Something went wrong reading the file");
        let input = contents.lines().flat_map(|t| t.parse::<u32>()).collect::<Vec<u32>>();
        
        b.iter(|| {
            part2(&input);
        });
    }
}

