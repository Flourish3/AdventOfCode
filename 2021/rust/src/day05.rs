//#![feature(test)]

//extern crate test;
use std::cmp;
use std::fs::File;
use std::io::prelude::*;
use std::{num::ParseIntError, str::FromStr};
use itertools::Itertools;
use std::hash::{Hash, Hasher};
use std::collections::HashSet;

#[derive(Debug, Clone, Copy)]
struct Point {
    x: f32,
    y: f32,
}

impl PartialEq for Point {
    fn eq(&self, other: &Self) -> bool {
        self.x == other.x && self.y == other.y
    }
}
  
impl Eq for Point {}

impl Hash for Point {
    fn hash<H: Hasher>(&self, state: &mut H) {
        (self.x as u32).hash(state);
        (self.y as u32).hash(state);
    }
}

impl FromStr for Point {
    type Err = ParseIntError;

    fn from_str(s: &str) -> Result<Self, ParseIntError> {
        match s.split_once(",") {
            Some((x, y)) => Ok(Point {
                x: x.parse().unwrap(),
                y: y.parse().unwrap(),
            }),
            None => panic!("Error parsing"),
        }
    }
}
#[derive(Clone, Debug)]
struct Line {
    from: Point,
    to: Point,
}

impl Line {
    fn line_coeff(&self) -> (f32, f32, f32) {
        (
            self.from.y - self.to.y,
            self.to.x - self.from.x,
            -1_f32 * (self.from.x * self.to.y - self.to.x * self.from.y),
        )
    }

    fn point_on_line(&self) -> HashSet<Point> {
        if self.from.x == self.to.x {
            let min_y = cmp::min(self.from.y as u32, self.to.y as u32);
            let max_y = cmp::max(self.from.y as u32, self.to.y as u32);

            (min_y..=max_y)
                .map(|y| Point{x:self.from.x, y: y as f32})
                .collect::<HashSet<Point>>()
        } else if self.from.y == self.to.y {
            let min_x = cmp::min(self.from.x as u32, self.to.x as u32);
            let max_x = cmp::max(self.from.x as u32, self.to.x as u32);

            (min_x..=max_x)
                .map(|x| Point{x:x as f32, y:self.from.y})
                .collect::<HashSet<Point>>()
        } else {
            let min_y = cmp::min(self.from.y as u32, self.to.y as u32);
            let max_y = cmp::max(self.from.y as u32, self.to.y as u32);

            let min_x = cmp::min(self.from.x as u32, self.to.x as u32);
            let max_x = cmp::max(self.from.x as u32, self.to.x as u32);

            let y_range: Vec<u32> = if self.from.y > self.to.y {
                (min_y..=max_y).rev().collect::<Vec<u32>>()
            } else {
                (min_y..=max_y).collect::<Vec<u32>>()
            };
            
            let x_range: Vec<u32> = if self.from.x > self.to.x {
                (min_x..=max_x).rev().collect::<Vec<u32>>()
            } else {
                (min_x..=max_x).collect::<Vec<u32>>()
            };
            
            x_range
                .iter()
                .zip(y_range)
                .map(|(a,b)| Point{x:*a as f32, y:b as f32})
                .collect()
        }
    }

    fn intersection(&self, other: &Line) -> HashSet<Point> {
        /* let l1_coeff = self.line_coeff();
        let l2_coeff = other.line_coeff();

        let d = l1_coeff.0 * l2_coeff.1 - l1_coeff.1 * l2_coeff.0;
        let dx = l1_coeff.2 * l2_coeff.1 - l1_coeff.1 * l2_coeff.2;
        let dy = l1_coeff.0 * l2_coeff.2 - l1_coeff.2 * l2_coeff.0;
        if d != 0_f32 {
            Some(Point {
                x: dx / d,
                y: dy / d,
            })
        } else {
            None
        } */
        let inter = self.point_on_line()
        .intersection(&other.point_on_line())
        .copied()
        .collect();
        //println!("{:?}", self);
        //println!("{:?} {:?} {:?}", self.point_on_line(), other.point_on_line(), inter);
        //println!("");

        inter
    }

    fn is_hor_or_diag(&self) -> bool {
        self.from.x == self.to.x || self.from.y == self.to.y
    }
}

fn main() {
    let mut contents = String::new();
    File::open("../data/05.txt")
        .expect("File not found")
        .read_to_string(&mut contents)
        .expect("Something went wrong when reading");
    let points = contents
        .lines()
        .flat_map(|line| match line.split_once(" -> ") {
            Some((first, second)) => Some((
                first.parse::<Point>().unwrap(),
                second.parse::<Point>().unwrap(),
            )),
            None => None,
        })
        .map(|(first, second)| Line {
            from: first,
            to: second,
        })
        //.filter(|line| !line.is_hor_or_diag())
        .combinations(2)
        .flat_map(|l| l[0].intersection(&l[1]))
        .unique()
        .collect::<Vec<Point>>();

    println!("Part 1: {}", points.len());

    
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_intersection() {
        let l1 = Line {
            from: Point { x: 0_f32, y: 0_f32 },
            to: Point {
                x: 10_f32,
                y: 10_f32,
            },
        };

        let l2 = Line {
            from: Point {
                x: 0_f32,
                y: 10_f32,
            },
            to: Point {
                x: 10_f32,
                y: 0_f32,
            },
        };

        //assert_eq!(l1.intersection(&l2), Some(Point { x: 5_f32, y: 5_f32 }));
    }

    #[test]
    fn test_point_on_line(){
        let l1 = Line {
            from: Point { x: 8_f32, y: 0_f32 },
            to: Point {
                x: 0_f32,
                y: 8_f32,
            },
        };

        println!("{:?}",l1.point_on_line())
    }
}
