function step(amount)
    -- amount количество повторений
    -- цикл работает от 1 до amount
    for i = 1, amount do
        turtle.forward()
    end
end

step(3) -- amount = 3
turtle.turnLeft()
step(5) -- amount = 5
turtle.turnLeft()
step(10) -- amount = 10


-- === Программа копания туннеля с постановкой факела ===
funcion placeTorch()   -- функция для установки факела
    turtle.select(1)   -- выбираем слот с факелом
    turtle.turnLeft()  -- поворт влево
    turtle.dig()       -- выкопать блок
    turtle.place()     -- ставим факел
    turtle.turnRight() -- поворт вправо
end

function tunnel(amount, torch_steps) -- функция копания туннеля (общая_длина, шагов_для_факела)
    steps = 0                        -- подсчет шагов для факела

    for i = 1, amount do             -- копаем туннель от 1 до общей длины
        turtle.dig()
        turtle.forward()
        turtle.digUp()
        steps = steps + 1            -- после каждого шага, увеличиваем шаг для факела

        if steps == torch_steps then -- если числа steps и torch_steps совпадают
            placeTorch()             -- вызываем функцию поставить факел
            steps = 0                -- обнуляем шаги, чтобы считать заново
        end
    end
end

tunnel(10, 2)   -- туннель на 10 блоков, факел после каждого второго
tunnel(30, 5)   -- туннель на 30 блоков, факел после каждого пятого
tunnel(100, 10) -- туннель на 100 блоков, факел после каждого десятого


-- Задача 1. Построить столбик любой высоты
funcion column(height)               -- column - высота столба
    turtle.select(1)                 -- выбрать слот с блоками

    for i = 1, height do             -- от 1 до высоты столба
        turtle.place()               -- ставим блок
        turtle.up()                  -- идем вверх
    end

    while not turtle.detectDown() do -- пока внизу нет блоков
        turtle.down()                -- идем вниз
    end
end

column(5)  -- столбик 5 блоков в высоту
column(3)  -- столбик 3 блока в высоту
column(10) -- столбик 10 блоков в высоту


-- Задача 2. Функция для прямоугольной платформы
function platform(length, width) -- length - длина, width - ширина

end

-- Задача 3. Функция, которая копает шахту 3х2 заданной длины и возвращается 
function cave(length) -- length - длина шахты

end

-- Задача 4. Функция, которая строит стену заданной высоты и длины
function wall(length, height) -- length - длина, height - высота

end

