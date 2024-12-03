pattern = ~r/mul\((\d+),(\d+)\)/

result = File.stream!("input.txt")
|> Enum.flat_map(fn line ->
    Regex.scan(pattern, line)
    |> Enum.map(fn [_, num1, num2] ->
        String.to_integer(num1) * String.to_integer(num2)
    end)
end)
|> Enum.sum()

IO.puts(result)
