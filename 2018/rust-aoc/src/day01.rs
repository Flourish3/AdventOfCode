#![feature(test)]
#![feature(cell_update)]

extern crate test;

use std::collections::HashSet;
use std::cell::Cell;
use std::fs::File;
use std::io::prelude::*;

fn part1(input: &str) -> i32 {
    input.lines().map(|t| t.parse::<i32>().unwrap()).sum()
}

fn part2(input: &str) -> i32 {
    let mut seen : HashSet<i32> = HashSet::new();
    let freq = Cell::new(0);

    input
        .lines()
        .map(|t| t.parse::<i32>().unwrap())
        .cycle()
        .take_while(|_| seen.insert(freq.get()))
        .for_each(|n| {
            freq.update(|old| old + n);
        });

    return freq.get();
}

fn main() {
    let mut contents = String::new();
    File::open("../data/input01.txt")
        .expect("File not found")
        .read_to_string(&mut contents)
        .expect("Something went wrong reading the file");

    println!("Part 1: {}", part1(&contents));
    println!("Part 2: {}", part2(&contents));
}

#[cfg(test)]
mod tests {
    use super::*;
    use test::{Bencher, black_box};

    #[test]
    fn test_p1(){
        assert_eq!(part1("+1\n+1\n+1"), 3);
        assert_eq!(part1("+1\n+1\n-2"), 0);
        assert_eq!(part1("-1\n-2\n-3"), -6);
    }

    #[test]
    fn test_p2(){
        assert_eq!(part2("+1\n-1"), 0);
        assert_eq!(part2("+3\n+3\n+4\n-2\n-4"), 10);
        assert_eq!(part2("-6\n+3\n+8\n+5\n-6"), 5);
        assert_eq!(part2("+7\n+7\n-2\n-7\n-4"), 14);
    }

    #[bench]
    fn bench_part1(b: &mut Bencher) {
        let mut contents = String::new();
        File::open("../data/input01.txt")
            .expect("File not found")
            .read_to_string(&mut contents)
            .expect("Something went wrong reading the file");

        b.iter(|| {
            part1(&contents);
        });
    }

    #[bench]
    fn bench_part2(b: &mut Bencher) {
        let mut contents = String::new();
        File::open("../data/input01.txt")
            .expect("File not found")
            .read_to_string(&mut contents)
            .expect("Something went wrong reading the file");

        b.iter(|| {
            part2(&contents);
        });
    }
}

