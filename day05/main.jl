function p1(filename)
    maps = [Dict() for _ in range(1,7)]

    seeds = NaN

    open(filename) do file
        level_count = 0
        for (i, line) in enumerate(eachline(file))
            if line == ""
                continue
            elseif i==1
                seeds = [parse(Int64, x) for x in split(split(line, ": ")[2], " ")]
            elseif occursin("map:", line)
                level_count += 1
                continue
            else
                numbers = [parse(Int64, x) for x in split(line, " ")]
                difference = numbers[1] - numbers[2]
                maps[level_count][(numbers[2], numbers[2]+numbers[3])] = difference
            end
        end


        result = Inf
        for seed in seeds

            a = seed
            for m in maps
                for (k, v) in m
                    if a > k[1] && a <= k[2]
                        a += v
                        break
                    end
                end
            end
            result = min(result, a)
        end
        return result
    end
    
end

function p2(filename)
    maps = [Dict() for _ in range(1,7)]

    seeds = NaN

    open(filename) do file
        level_count = 0
        for (i, line) in enumerate(eachline(file))
            if line == ""
                continue
            elseif i==1
                seeds = [parse(Int64, x) for x in split(split(line, ": ")[2], " ")]
            elseif occursin("map:", line)
                level_count += 1
                continue
            else
                numbers = [parse(Int64, x) for x in split(line, " ")]
                difference = numbers[2] - numbers[1]
                maps[level_count][(numbers[1], numbers[1]+numbers[3])] = difference
            end
        end
    end
        
    start = 0
    while true
        a = start
        rev_maps = reverse(maps)
        a = traverse_map(a, rev_maps)
        for i in range(1, length(seeds))
            if i % 2 == 1
                if a >= seeds[i] && a < (seeds[i] + seeds[i+1])
                    @goto escape_label
                end
            end
        end
        
        start += 1

        if start % 100000 == 0
            println(start)
        end

    end

    @label escape_label
    return start
    
end

@inline function traverse_map(a, reverse_maps)
    for m in reverse_maps
        for k in keys(m)
            if a >= k[1] && a < k[2]
                a += m[k]
                break
            end
        end
    end
    return a
end



@time println(p1("day05/test.txt"))
@time println(p1("day05/input.txt"))
println("*******************************")
@time println(p2("day05/test.txt"))
@time println(p2("day05/input.txt"))
