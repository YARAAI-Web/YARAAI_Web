rule auto_rule_20250726130148_6809 {
  strings:
    $o0 = "dword_4C18B0" wide ascii nocase
    $o1 = "compiled" wide ascii nocase
    $o2 = "dword_4C12D0" wide ascii nocase
    $o3 = "MapVirtualKeyW" wide ascii nocase
    $o4 = "dword_4C1290" wide ascii nocase
  condition:
    4 of ($o*)
}