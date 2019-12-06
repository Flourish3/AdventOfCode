module Main where

import Data.List (sort, nub)

main :: IO ()
main = do
    xs <- parseInput <$> readFile "data/day04.txt"
    print $ length $ filter allUnique xs
    print $ length $ filter noAnagram xs
    let str = [["zyx","vcba","ajshd", "vcba"],["v","oi","poad","io"],["hello"]]
    print $ length $ filter (\l -> length l == length (nub (map sort l))) str


parseInput :: String -> [[String]]
parseInput s = map words (lines s)

allUnique :: Ord a => [a] -> Bool
allUnique l = length l == length (nub l)

noAnagram :: Ord a => [[a]] -> Bool
noAnagram l = allUnique (map sort l)
