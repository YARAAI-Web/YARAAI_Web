rule auto_rule_20250726092311_1582 {
  strings:
    $o0 = "cbOverhead" wide ascii nocase
    $o1 = "UsedDefaultChar" wide ascii nocase
    $o2 = "x21A70032729DLL" wide ascii nocase
    $o3 = "x24C3" wide ascii nocase
    $o4 = "dword_41222C" wide ascii nocase
  condition:
    4 of ($o*)
}