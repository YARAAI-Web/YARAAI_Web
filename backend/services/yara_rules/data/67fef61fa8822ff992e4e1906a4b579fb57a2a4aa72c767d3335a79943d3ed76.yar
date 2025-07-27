rule auto_rule_20250726233333_9235 {
  strings:
    $o0 = "xDAFu" wide ascii nocase
    $o1 = "x6932" wide ascii nocase
    $o2 = "xF89C85B5" wide ascii nocase
    $o3 = "dword_426000" wide ascii nocase
  condition:
    4 of ($o*)
}