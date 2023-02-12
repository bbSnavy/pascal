import Data.List (intercalate)

level 1 = [1]
level n = do
  let v = wrap (level (n - 1)) n
  [(v !! (i - 0)) + (v !! (i - 1)) | i <- [1 .. n]]

wrap list size = [0] ++ list ++ [0]

pascal n = map level [1 .. n]

main =
  putStrLn
    (intercalate "\n" [show v | v <- pascal 15])