rule auto_rule_20250726133004_1260 {
  strings:
    $o0 = "dword_42A020" wide ascii nocase
    $o1 = "dword_45CF08" wide ascii nocase
    $o2 = "_bittestandset" wide ascii nocase
    $o3 = "hard" wide ascii nocase
  condition:
    4 of ($o*)
}