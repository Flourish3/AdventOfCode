#![feature(option_result_contains)]
#![feature(test)]
#![feature(slice_group_by)]

extern crate test;
use std::fs::File;
use std::io::prelude::*;
use std::collections::HashMap;
use regex::Regex;
use itertools::Itertools;

type RuleId = usize;
type Rules = HashMap<RuleId, Rule>;


struct Chart {
    n: usize,
    rows: Vec<Vec<Vec<bool>>>
}

#[derive(Debug, PartialEq)]
enum RuleType {
    Terminal,
    Binary
}

#[derive(Debug)]
struct Rule {
    rule_id: RuleId,
    rule_type: RuleType,
    rule: Option<Vec<Vec<RuleId>>>,
    symbol: Option<char>
}

impl PartialEq for Rule {
    fn eq(&self, other: &Rule)-> bool {
        self.rule_id == other.rule_id &&
        self.symbol == other.symbol &&
        self.rule_type == other.rule_type
    }
}


fn parse_rule(rule_str: &str) -> Rule {
    let terminal_re = Regex::new(r#""(\S)""#).unwrap();

    let (rule_id, rule) = match rule_str.split_once(": ") {
        Some((rule_id, rules)) => {
            let id = rule_id.parse::<RuleId>().unwrap();
            
            (id, rules)
        }
        None => panic!("couldn't parse rule {0}", rule_str)
    };

    match terminal_re.captures(rule).map(|c| c.get(0)).flatten() {
        Some(symbol) => 
            Rule {
                rule_id: rule_id,
                rule_type: RuleType::Terminal,
                rule: None,
                symbol: symbol.as_str().chars()
                    .collect::<Vec<char>>()
                    .iter().nth(1).copied(),
            },

        None => {
            println!("{}", rule);
            let split = rule
            .split(" | ")
            .map(|sub_rules| sub_rules
                .split(" ")
                .map(|i| i.parse::<RuleId>()
                .unwrap())
                .collect::<Vec<RuleId>>())
            .collect::<Vec<Vec<RuleId>>>();
            
           
            Rule {
                rule_id: rule_id,
                rule_type: RuleType::Binary,
                rule: Some(split),
                symbol: None,
            }
        },
    }
}

fn parse_rules(rule_str: &str) -> Rules {
    let mut rule_map: HashMap<RuleId, Rule> = HashMap::new();

    rule_str
        .lines()
        .map(|rule_str| parse_rule(rule_str))
        .for_each(|rule: Rule| {
            rule_map.insert(rule.rule_id, rule);
            ()
        });

        rule_map
}

fn cyk(entry: &str, terminal_rules: &Vec<&Rule>, binary_rules: &Vec<&Rule>)-> bool {
    let chars = entry.chars().collect::<Vec<char>>();
    let n = chars.len();
    let mut rows: Vec<Vec<Vec<bool>>> = Vec::with_capacity(n);
    for _ in 0..n {
        let mut inter_vec : Vec<Vec<bool>> = Vec::with_capacity(n);
        for _ in 0..n{
            inter_vec.push(vec![false;terminal_rules.len() + binary_rules.len() + 2]);
        }
        rows.push(inter_vec);
    }

    

    let mut chart = Chart{
        n: n,
        rows: rows
    };

    for i in 0..n {
        match terminal_rules
            .iter()
            .find(|r| r.symbol == Some(chars[i])) {
                Some(rule) => chart.rows[0][i][rule.rule_id] = true,
                None => (),
            }
            
    }


    for l in 2..=n { 
        for i in 1..=(n - l + 1) { 
            for k in 1..=l-1 { // split width / row

               /*  if l == 3 && i == 2{
                println!("Checking for combination {0:?}-{1:?}",chart.rows[k-1][i-1],chart.rows[l-k-1][i+k-1]  )
                } */

                for rule in binary_rules{
                    /* if l == 3 && i == 2{
                        println!("Checking rule {0}", rule.rule_id);
                    } */
                    let mut b = false;
                    for sub_rules in rule.rule.as_ref().unwrap() {
                        /* if l == 3 && i == 2{
                            println!("{:?}", rule);
                            println!("first: {0:?}, {1:?}", sub_rules[0],chart.rows[k-1][i-1][sub_rules[0]]);
                            println!("second: {0:?}, {1:?}", sub_rules[1],chart.rows[l-k-1][i+k-1][sub_rules[1]]);

                        } */

                        b = b || chart.rows[k-1][i-1][sub_rules[0]] && chart.rows[l-k-1][i+k-1][sub_rules[1]];
                    }

                    chart.rows[l-1][i-1][rule.rule_id] |= b
                }
                /* if l == 3 && i == 2{
                    println!("")
                }
 */
               /*  let rule_match = binary_rules.iter()
                    .find(|r| r.rule.as_ref().map(|sub_rules| {
                    
                        let mut b = false;
                        for s in sub_rules {
                            b |= chart.rows[k-1][i-1][s[0]] && chart.rows[l-k-1][i+k-1][s[1]];
                        }
                        
                    
                        
                        b
                    }).unwrap_or_else(|| false)
                );

                match rule_match {
                    Some(rule) => chart.rows[l-1][i-1][rule.rule_id] = true,
                    None => (),
                    //None => println!("No match for first check: {0:?}, second check{1:?}", (k,i), ((l-1)-(k+1), i+(k+1))),
                }
                 */
            }
        }
    }

    let is_match = chart.rows[chart.n-1][0][0];
    println!("{0} --- {1}", entry, if is_match {"MATCH"} else {"NO MATCH"});

    is_match
}

fn main() {
    let mut contents = String::new();
    File::open("../data/19.txt")
        .expect("File not found")
        .read_to_string(&mut contents)
        .expect("Something went wrong reading the file");

    let (rules, entries) = match contents.split_once("\n\n") {
        Some((rules, entries)) => (parse_rules(rules), entries.lines()),
        None => panic!("Couldn't parse input file {0}", "../data/19.txt"),
    };

/*     let r = rules.values()
    .filter(|v| v.rule_type == RuleType::Binary)
    .map(|r| r.rule.as_ref().unwrap())
    .flatten()
    //.collect::<Vec<&Vec<RuleId>>>()
    .group_by(|pair| {
        println!("{:?}", pair);
        format!("{0} {1}", pair[0], pair[1])
    });

    for (key, group) in &r {
        println!("{0} {1:?}", key, group.collect::<Vec<&Vec<RuleId>>>());
    } */

    let terminal_rules = rules.values()
    .filter(|v| v.rule_type == RuleType::Terminal)
    .collect::<Vec<&Rule>>();

    let binary_rules = rules.values()
        .filter(|v| v.rule_type == RuleType::Binary)
        .collect::<Vec<&Rule>>();

    let matching = entries
        .filter(|entry| cyk(*entry, &terminal_rules, &binary_rules))
        .collect::<Vec<&str>>()
        .len();

    println!("Found {} lines matching rules", matching);
}

#[cfg(test)]
mod tests {
    use super::*;
    use test::{Bencher};

    #[test]
    fn test_rule_parse_terminal(){
        assert_eq!(parse_rule(r#"4: "a""#), Rule{
            rule_id: 4,
            rule_type: RuleType::Terminal,
            rule: None,
            symbol: Some('a'),
        })
    }

    #[test]
    fn test_rule_parse_binary(){
        assert_eq!(parse_rule(r#"1: 2 3 | 3 2"#), Rule{
            rule_id: 1,
            rule_type: RuleType::Binary,
            rule: Some(vec![vec![2,3],vec![3,2]]),
            symbol: None,
        })
    }

    #[test]
    fn test_cyk(){
        let mut contents = String::new();
        File::open("../data/19.txt")
            .expect("File not found")
            .read_to_string(&mut contents)
            .expect("Something went wrong reading the file");
    
        let (rules, _entries) = match contents.split_once("\n\n") {
            Some((rules, entries)) => (parse_rules(rules), entries.lines()),
            None => panic!("Couldn't parse input file {0}", "../data/19.txt"),
        };

        let terminal_rules = rules.values()
        .filter(|v| v.rule_type == RuleType::Terminal)
        .collect::<Vec<&Rule>>();
    
        let binary_rules = rules.values()
            .filter(|v| v.rule_type == RuleType::Binary)
            .collect::<Vec<&Rule>>();

        let entry = "baabbbabbbaababbbabababbaabababbbbbabbbbbabbaabaabaabababbabbaaabbbbabaabbabbbbaaabbaaaabababaab"; 
        assert_eq!(cyk(entry, &terminal_rules, &binary_rules), false)

    }

    #[bench]
    fn bench_part1(b: &mut Bencher) {
        let mut contents = String::new();
        File::open("../data/19.txt")
            .expect("File not found")
            .read_to_string(&mut contents)
            .expect("Something went wrong reading the file");
    
        let (rules, _entries) = match contents.split_once("\n\n") {
            Some((rules, entries)) => (parse_rules(rules), entries.lines()),
            None => panic!("Couldn't parse input file {0}", "../data/19.txt"),
        };

        let entry = "baabbbabbbaababbbabababbaabababbbbbabbbbbabbaabaabaabababbabbaaabbbbabaabbabbbbaaabbaaaabababaab"; 
        let terminal_rules = rules.values()
        .filter(|v| v.rule_type == RuleType::Terminal)
        .collect::<Vec<&Rule>>();
    
        let binary_rules = rules.values()
            .filter(|v| v.rule_type == RuleType::Binary)
            .collect::<Vec<&Rule>>();

        b.iter(|| {
            cyk(entry, &terminal_rules, &binary_rules);
        });
    }
}
