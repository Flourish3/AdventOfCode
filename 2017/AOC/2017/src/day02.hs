module Main where

import Data.List (delete)

main :: IO ()
main = do
    xs <- parseInput <$> readFile "data/day02.txt"
    print (sum (map checksum1 xs))
    print (sum (map checksum2 xs))



parseInput :: String -> [[Int]]
parseInput = map (map read . words) . lines

checksum1 :: [Int] -> Int
checksum1 xs = maximum xs - minimum xs

checksum2 :: [Int] -> Int
checksum2 xs =
    head [ q | x <- xs, y <- delete x xs, (q,0) <- [x `divMod` y] ]


