#![feature(test)]

extern crate test;

use std::fs::File;
use std::io::prelude::*;
use std::{num::ParseIntError, str::FromStr};

trait LastToDigit {
    fn last_digit(&self) -> u32;
}

impl LastToDigit for &str {
    fn last_digit(&self) -> u32 {
        self.chars()
            .last()
            .map(|s_opt| s_opt.to_digit(10).unwrap())
            .unwrap()
    }
}

enum Direction {
    Forward(u32),
    Down(u32),
    Up(u32),
}

impl FromStr for Direction {
    type Err = ParseIntError;

    fn from_str(s: &str) -> Result<Self, ParseIntError>{
        let (direction, units) = s.split_once(" ").unwrap();
        let units = units.parse()?;

        Ok(match direction {
            "forward" => Self::Forward(units),
            "down" => Self::Down(units),
            "up" => Self::Up(units),
            _ => unreachable!()
        })
    }
}

fn main() {
    let mut contents = String::new();
    File::open("../data/02.txt")
        .expect("File not found")
        .read_to_string(&mut contents)
        .expect("Something went wrong when reading");

    let (forward, rest): (Vec<&str>, Vec<&str>) = contents
        .lines()
        .partition(|inst| inst.chars().nth(0) == Some('f'));

    let hor_pos = forward.iter().map(|s| s.last_digit()).sum::<u32>();
    let (up, down): (Vec<&str>, Vec<&str>) =
        rest.iter().partition(|s| s.chars().nth(0) == Some('u'));

    let vert_pos = down.iter().map(|s| s.last_digit()).sum::<u32>()
        - up.iter().map(|s| s.last_digit()).sum::<u32>();

    println!(
        "Part 1 {0}, {1}, {2}",
        hor_pos,
        vert_pos,
        hor_pos * vert_pos
    );

    let (mut aim, mut depth) = (0, 0);
    for line in contents.lines() {
        match line.chars().next() {
            Some('u') => aim -= line.last_digit(),
            Some('d') => aim += line.last_digit(),
            Some('f') => depth += aim * line.last_digit(),
            _ => (),
        }
    }

    println!("Part 1 {0}, {1}, {2}", hor_pos, depth, hor_pos * depth);

    let dirs: Vec<Direction> = contents
        .lines()
        .map(|l| l.parse::<Direction>().unwrap()).collect();

    let (h,a,d) = dirs
        .iter()
        .fold((0,0, 0), |(h, a, d), direction| match direction{
            Direction::Forward(units) => (h+units, a, d+(a*units)),
            Direction::Down(units) => (h, a+units,d),
            Direction::Up(units) => (h, a-units, d),
        });
    println!("{0}, {1}, {2}", h,a,d);

}

#[cfg(test)]
mod tests {
    use super::*;
    use test::Bencher;

    #[bench]
    fn bench_depth(b: &mut Bencher) {
        let mut contents = String::new();
        File::open("../data/02.txt")
            .expect("File not found")
            .read_to_string(&mut contents)
            .expect("Something went wrong when reading");

        b.iter(|| {
            let (mut aim, mut depth) = (0, 0);
            for line in contents.lines() {
                match line.chars().next() {
                    Some('u') => aim -= line.last_digit(),
                    Some('d') => aim += line.last_digit(),
                    Some('f') => depth += aim * line.last_digit(),
                    _ => (),
                }
            }
        })
    }
}
