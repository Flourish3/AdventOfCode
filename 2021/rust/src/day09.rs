//#![feature(test)]

//extern crate test;

use std::fs::File;
use std::io::prelude::*;

fn get_total_risk_level(lows: Vec<u32>) -> u32 {
    lows.iter().sum::<u32>() + lows.len() as u32
}

fn find_low_point_values(map: Vec<Vec<u32>>) -> Vec<u32> {
    let max_y = map.len();
    let max_x = map[0].len();

    let mut ret: Vec<u32> = Vec::new();

    for y in 0..max_y {
        for x in 0..max_x {
            let mut is_smallest = true;
            let current = map[y][x];
            // Check above
            if y > 0 {
                is_smallest &= current < map[y-1][x];
            }

            // Check below
            if y < max_y - 1 {
                is_smallest &= current < map[y+1][x];
            }

            // Check left
            if x > 0 {
                is_smallest &= current < map[y][x-1];
            }

            // Check right
            if x < max_x - 1 {
                is_smallest &= current < map[y][x+1]
            }

            if is_smallest {
                ret.push(current);
            }
        }
    }
    ret
}

fn parse_input(st: &String) -> Vec<Vec<u32>> {
    st
        .lines()
        .map(|l| l.chars().map(|c| c.to_digit(10).unwrap()).collect())
        .collect()
}

fn main() {
    let mut contents = String::new();
    File::open("../data/09.txt")
        .expect("File not found")
        .read_to_string(&mut contents)
        .expect("Something went wrong when reading");
    
    let input = parse_input(&contents);
    let low_points = find_low_point_values(input);

    println!("Part 1 {}", get_total_risk_level(low_points))
    
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_input_parse(){
        let contents = String::from("2199943210\n3987894921\n9856789892\n8767896789\n9899965678");

        assert_eq!(parse_input(&contents), vec![
            vec![2,1,9,9,9,4,3,2,1,0],
            vec![3,9,8,7,8,9,4,9,2,1],
            vec![9,8,5,6,7,8,9,8,9,2],
            vec![8,7,6,7,8,9,6,7,8,9],
            vec![9,8,9,9,9,6,5,6,7,8]
        ])
    }

    #[test]
    fn test_example_part_1(){
        let contents = String::from("2199943210\n3987894921\n9856789892\n8767896789\n9899965678");
        let i = parse_input(&contents);
        let lows = find_low_point_values(i);
        
        assert_eq!(lows, vec![1,0,5,5]);
        assert_eq!(get_total_risk_level(lows), 15);
    }

}
