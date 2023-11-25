//#![feature(test)]

//extern crate test;

use std::fs::File;
use std::io::prelude::*;
use std::collections::HashMap;
use itertools::Itertools;

fn run_population_calc(initial: Vec<u8>) -> usize {
    let mut p: HashMap<u8, usize> = HashMap::new();
    for i in 0..=8 {
        p.insert(i,0);
    }
    let mut e = initial.clone();
    e.sort();
    for (k,v) in &e.into_iter().group_by(|x| x.clone()) {
        let a = v.collect::<Vec<u8>>();
        println!("{:?}",a);
        p.insert(k,a.len());
    }

    println!("{:?}", p);


    for i in 0..256 {
        let c = p.clone();
        let mut m = c.iter().collect::<Vec<(&u8,&usize)>>();
        let eights = *p.get(&8).unwrap();
        m.sort();
        for (k,v) in m.iter() {
            if **k == 8 {
                p.insert(7, eights);
            } else {
                let index: u8 = ((((**k) as i8) + 8) % 9) as u8;
                //println!("index {}, new value: {}, k: {}", index, new_v, k);

                if index == 6{
                    let old_six = *p.get(&6).unwrap();
                    p.insert(6, old_six + **v);
                } else if index == 8 {
                    p.insert(index, **v);
                    p.insert(6, **v);
                } else {
                    p.insert(index, **v);
                }

            }
        }
        println!("{:?}", p);
    }
    p.values().sum()
}

fn run_population(initial: Vec<u8>) -> usize {
    let mut pop = initial.clone();
    let mut prev = initial.len();

    for i in 0..80 {
        pop = pop.iter().flat_map(|fish| {
            if *fish == 0 {
                vec![6, 8]
            } else {
                vec![fish - 1]
            }
        }).collect();
       // println!("iteration: {}, prev count: {}, count: {}, diff {}", i,prev, pop.len(), pop.len() - prev);
        prev = pop.len();
    }

    pop.len()
}

fn main() {
    let mut contents = String::new();
    File::open("../data/06.txt")
        .expect("File not found")
        .read_to_string(&mut contents)
        .expect("Something went wrong when reading");
    let initial: Vec<u8> = contents
        .split(",")
        .map(|x| x.parse::<u8>().unwrap())
        .collect();

    println!("Part 1 {}", run_population_calc(initial));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_example() {
        let state = vec![3, 4, 3, 1, 2];
        assert_eq!(run_population(state), 5934);
    }

    #[test]
    fn test_example_two(){
        let state = vec![3, 4, 3, 1, 2];
        assert_eq!(run_population_calc(state), 5934);
    }
}
