; Paste this into: Printer Settings > Machine G-code > Layer change G-code
G91               
G1 Z1.5 F6000     ; Lift the nozzle UP by 1.5mm 
G90               
G1 X5 Y180 F18000 ;Goes to switch
G1 X-2 F3000      ; Move slowly backward to actually click the switch
G4 P1200          ; Freezes for 1.2 seconds
G1 X10 F18000     ; away from the switch
G91               ; Goes back to where it was
G1 Z-1.5 F6000    ; Drop the nozzle exactly 1.5mm 
G90               ; printer can resume printing
