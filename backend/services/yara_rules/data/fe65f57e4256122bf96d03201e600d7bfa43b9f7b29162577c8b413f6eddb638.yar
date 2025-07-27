rule auto_rule_20250726205357_2126 {
  strings:
    $o0 = "xB23B8F0900000000uLL" wide ascii nocase
    $o1 = "dword_4296F8" wide ascii nocase
    $o2 = "dword_42959C" wide ascii nocase
    $o3 = "x7913u" wide ascii nocase
    $o4 = "dword_429578" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726205401_2926 {
  strings:
    $o0 = "x442" wide ascii nocase
    $o1 = "dword_4294DC" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726205404_4669 {
  condition:
    auto_rule_20250726205357_2126 or auto_rule_20250726205401_2926
}