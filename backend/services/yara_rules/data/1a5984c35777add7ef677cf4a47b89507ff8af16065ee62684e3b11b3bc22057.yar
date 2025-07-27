rule auto_rule_20250726183451_6473 {
  strings:
    $o0 = "dword_404206" wide ascii nocase
    $o1 = "szKey" wide ascii nocase
    $o2 = "xFFFFFF87" wide ascii nocase
    $o3 = "dword_40418E" wide ascii nocase
  condition:
    4 of ($o*)
}