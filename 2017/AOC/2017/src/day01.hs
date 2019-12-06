{-# LANGUAGE NegativeLiterals #-}

module Main(main) where

import Data.Char (digitToInt)

main :: IO ()
main = do
  digits <- readFile "data/day01.txt"
  print $ part1 digits
  print $ part2 digits

part1 :: String -> Int
part1 digits = solve 1 digits

part2 :: String -> Int
part2 digits = solve (length digits `div` 2) digits

solve :: Int -> String -> Int
solve n digits = sum ( zipWith (\a b -> if a == b then digitToInt a else 0) digits (drop n (cycle digits)))