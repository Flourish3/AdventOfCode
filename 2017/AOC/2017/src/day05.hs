module Main where

main :: IO()
main = do
    jumps <- parseInput <$> readFile "data/day05.txt"

    print (jumps)

parseInput :: String -> [Int]
parseInput s = map read (lines s)

--Update rules
part1 :: Int -> Int
part1 x = x+1