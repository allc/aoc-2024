pattern = ~r/do\(\)|don't\(\)|mul\((\d+),(\d+)\)/

result = 0
yea = true

content = File.stream!("input.txt")
|> Enum.join("")

{result, _} = Regex.scan(pattern, content)
|> Enum.reduce({result, yea}, fn
    ["don't()"], {result, _} ->
        {result, false}
    ["do()"], {result, _} ->
        {result, true}
    [_, num1, num2], {result, yea} ->
        if yea do
            {result + String.to_integer(num1) * String.to_integer(num2), yea}
        else
            {result, yea}
        end
end)

IO.puts(result)
