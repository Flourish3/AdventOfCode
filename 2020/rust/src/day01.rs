use std::fs::File;
use std::io::prelude::*;
use itertools::Itertools;


fn _part1_old(input: &Vec<u32>) -> u32 {
    for combo in input.iter().copied().combinations(2) {
        let sum: u32 = combo.iter().sum();
        if sum == 2020{
            let product: u32 = combo.iter().product();
            return product;
        }
    }

    0
}

fn part1(input: &Vec<u32>) -> u32 {
    return input
        .iter()
        .copied()
        .combinations(2)
        .map(|combo| combo.iter().sum())
        .filter(|sum: &u32| *sum == 2020_u32)
        .take(1)
        .next()
        .unwrap();
}

fn main() {
    let mut contents = String::new();
    File::open("../data/01.txt")
        .expect("File not found")
        .read_to_string(&mut contents)
        .expect("Something went wrong reading the file");
    let input = contents.lines().flat_map(|t| t.parse::<u32>()).collect::<Vec<u32>>();

    println!("Part 1: {}", part1(&input));
}

mod tests {
    use super::*;

    #[test]
    fn test_p1_example(){
        assert_eq!(part1(&vec!(1721_u32,
            979_u32,
            366_u32,
            299_u32,
            675_u32,
            1456_u32)), 514579);
    }

}