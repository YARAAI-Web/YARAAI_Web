rule auto_rule_20250726190055_3465 {
  strings:
    $o0 = "x481D00000503LL" wide ascii nocase
    $o1 = "dword_42E6ED" wide ascii nocase
    $o2 = "x481D00000403LL" wide ascii nocase
    $o3 = "xF0Fu" wide ascii nocase
    $o4 = "xFBC676A9" wide ascii nocase
  condition:
    4 of ($o*)
}