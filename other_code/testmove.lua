scriptId = 'com.hackuiowa.move'
	scriptTitle = "move script"
	scriptDetailsUrl = ""
    appTitle = ""


    centerZoom = 0
    zoomIn = 0
    zoomOut = 0
    scrollSpeed = 10
    zoomCount = 0


    mouseEnabled = true
    --control mouse when inside appropriate window
    function onForegroundWindowChange(app, title)  
        myo.debug("onForegroundWindowChange: " .. app .. ", " .. title)
        appTitle = title
        local titleMatch = string.match(title, "testingForce") ~= nil
        --myo.controlMouse(titleMatch)
        myo.controlMouse(true)
        mouseEnabled = myo.mouseControlEnabled()

        --return titleMatch
        return true
    end
    
    function onPoseEdge(pose, edge)  
        myo.debug("onPoseEdge: " .. pose .. ": " .. edge)

        --make work for left or right
        pose = conditionallySwapWave(pose)

        local keyEdge = edge == "off" and "up" or "down"

        --do when pose is started
        if (edge == "on" or edge == "off") then
            if (pose == "waveOut") then
                onWaveOut(keyEdge)    
            elseif (pose == "waveIn") then
                onWaveIn(keyEdge)
            elseif (pose == "fist") then
                onFist(keyEdge)
            elseif (pose == "fingersSpread") then
                onFingersSpread(keyEdge)   
            end
        end

        --lock out poses when not doing anything
        if(pose ~= "rest" and pose ~= "unknown") then
            myo.unlock(edge == "off" and "timed" or "hold")
        end

    end

    --scroll out
    function onWaveOut(keyEdge)  
        myo.debug("Next")
        myo.vibrate("short")
        --set scroll out
        if (keyEdge == "down") then
            zoomOut = 1
        elseif(keyEdge == "up") then
            zoomOut = 0
            zoomCount = 0
        end
        --myo.keyboard("tab", keyEdge)
    end

    --scroll in
    function onWaveIn(keyEdge)  
        myo.debug("Previous")  
        myo.vibrate("short") 
        --set scroll in
        if (keyEdge == "down") then
            zoomIn = 1
        elseif(keyEdge == "up") then
            zoomIn = 0
            zoomCount = 0
        end


        --myo.keyboard("tab", keyEdge,"shift")
    end

    --move graph or/and move mouse
    function onFist(keyEdge)  
        myo.debug("Enter" .. keyEdge)  
        myo.vibrate("long")
        myo.mouse("left",keyEdge)
    end

    --reset zoom
    function onFingersSpread(keyEdge)  
        myo.debug("Escape") 
        myo.vibrate("short")
        myo.mouse("left","click")
    end 

    function onUnlock()  
        myo.debug("tap") 
    end 

    --clean up just in case
    function onLock()  
        myo.debug("tap") 
       -- myo.vibrate("long")
        escape()
        --myo.keyboard("escape", keyEdge)
    end 

    function escape()
        zoomIn = 0
        zoomOut = 0
        zoomCount = 0
    end

    function conditionallySwapWave(pose)  
        if myo.getArm() == "left" then
            if pose == "waveIn" then
                pose = "waveOut"
            elseif pose == "waveOut" then
                pose = "waveIn"
            end
        end
        return pose
    end

    function activeAppName()
        return appTitle
    end

    function onPeriodic()
        if (zoomIn == 1) then
            zoomCount = zoomCount + 1
            if zoomCount >= scrollSpeed then
               -- centerZoom = centerZoom + 1
                myo.mouseScrollBy(1)
                zoomCount = 0
            end
        elseif (zoomOut == 1) then
            zoomCount = zoomCount + 1
            if zoomCount >= scrollSpeed then
               -- centerZoom = centerZoom - 1
                myo.mouseScrollBy(-1)
                zoomCount = 0
            end
        end
    end


