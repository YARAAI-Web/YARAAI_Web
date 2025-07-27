rule auto_rule_20250726210303_9226 {
  strings:
    $o0 = "xF89C853C" wide ascii nocase
    $o1 = "x8E12FEB8" wide ascii nocase
    $o2 = "dword_433693" wide ascii nocase
    $o3 = "dword_413BB0" wide ascii nocase
    $o4 = "LoadBitmapA" wide ascii nocase
  condition:
    4 of ($o*)
}