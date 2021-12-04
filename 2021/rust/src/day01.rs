#![feature(test)]

extern crate test;

use std::fs::File;
use std::io::prelude::*;


fn count_seq_elems_larger(elems: &Vec<i64>) -> usize {
    let mut rotated = elems.iter().copied().collect::<Vec<i64>>();
    rotated.rotate_right(1);

    elems.iter().zip(&rotated)
        .skip(1)
        .map(|(x,y)| *x > *y)
        .filter(|l| *l)
        .count()
}

fn depth(vec: &[i64]) -> usize {
    vec.windows(2).filter(|w| w[1] > w[0]).count()
}

fn depth_two(vec: &[i64]) -> usize {
    vec.windows(4).filter(|w| w[3] > w[0]).count()
}

fn main() {
    let mut contents = String::new();
    File::open("../data/01.txt")
        .expect("File not found")
        .read_to_string(&mut contents)
        .expect("Something went wrong when reading");
    
    let measurements = contents.lines()
        .map(|l| l.parse::<i64>().unwrap())
        .collect::<Vec<i64>>();

            
    println!("Part 1 {}", depth(&measurements));    
    println!("Part 2 {}", depth_two(&measurements));

}

#[cfg(test)]
mod tests {
    use super::*;
    use test::{Bencher};

    #[bench]
    fn bench_window(b: &mut Bencher){
        let mut contents = String::new();
        File::open("../data/01.txt")
            .expect("File not found")
            .read_to_string(&mut contents)
            .expect("Something went wrong when reading");
        
        let measurements = contents.lines()
            .map(|l| l.parse::<i64>().unwrap())
            .collect::<Vec<i64>>();
            
        b.iter(|| depth(&measurements));
    }

    #[bench]
    fn bench_rotate(b: &mut Bencher){
        let mut contents = String::new();
        File::open("../data/01.txt")
            .expect("File not found")
            .read_to_string(&mut contents)
            .expect("Something went wrong when reading");
        
        let measurements = contents.lines()
            .map(|l| l.parse::<i64>().unwrap())
            .collect::<Vec<i64>>();
        b.iter(|| count_seq_elems_larger(&measurements));
    }
}