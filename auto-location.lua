--connect to client
local client, err = socket.tcp("127.0.0.1", 5000)
if not client then
    print("Connection failed:", err)
    return
end
print("Connected to Python!")

--init variables
local SCENE_ADDRESS = 0x801C8544
local CHEST_ADDRESS = 0x800084B8

local data = {
	game = "",
	scene = nil,
	previousScene = -1
}

function updateScene(scene_adr)
	if memory.read_u16(SCENE_ADDRESS) == 0x0801 then
		data.scene = memory.read_u16(0x803E6BC4)
	else
		data.scene = memory.read_u16(SCENE_ADDRESS)
	end
	
	if data.scene ~= data.previousScene then
		socket.sleep(1)
	end
		
	if memory.read_u16(SCENE_ADDRESS) == 0x0801 then
		data.scene = memory.read_u16(0x803E6BC4)
		data.game = "mm"
	else
		data.scene = memory.read_u16(SCENE_ADDRESS)
		data.game = "oot"
	end
	
    if data.scene ~= data.previousScene then

		local message = string.format(
			"scene=0x%04x|previousScene=0x%04x|game=%s\n",
			data.scene,
			data.previousScene,
			data.game
		)
        client:send("scene_changed|" .. message)
		
    end
    data.previousScene = data.scene
end

function updateChest(chest_adr)
	data.chest = memory.read_u16(chest_adr)
	if data.chest == 0xf5d5 then
		print("chest opened")
	end
end

--main loop
while true do
    
	updateScene(SCENE_ADDRESS)
	--updateChest(CHEST_ADDRESS)
    socket.sleep(0.1)
end

