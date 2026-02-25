-- if условие then
--     набор инструкций

turtle.detect() -- проверить блок впереди
turtle.detectDown() -- проверить блок снизу
turtle.detectUp() -- проверить блок сверху

-- если впереди есть блок тогда
if turtle.detect() then
    turtle.dig()        -- копаем его
else                    -- а если нет
    turtle.forward()    -- идем вперед
end                     -- конец

