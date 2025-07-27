rule auto_rule_20250726213700_7503 {
  strings:
    $o0 = "StrCatBuffW" wide ascii nocase
    $o1 = "lpfn" wide ascii nocase
    $o2 = "cAccel" wide ascii nocase
    $o3 = "StrToIntExA" wide ascii nocase
    $o4 = "EnumWindowStationsW" wide ascii nocase
  condition:
    4 of ($o*)
}