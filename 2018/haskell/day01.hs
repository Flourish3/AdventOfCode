import qualified Data.IntSet as S

main :: IO ()
main = do
    changes <- parseInput <$> readFile "../data/input01.txt"
    print $ part1 changes
    print $ part2 changes

parseInput :: String -> [Int]
parseInput =  map (read . filter (/= '+')) . lines

part1 :: [Int] -> Int
part1 = sum

part2 :: [Int] -> Int
part2 = go S.empty . scanl (+) 0 . cycle
    where go s (x:xs)
              | x `S.member` s = x
              | otherwise = go (S.insert x s) xs