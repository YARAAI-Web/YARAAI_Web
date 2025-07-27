rule auto_rule_20250726220352_8456 {
  strings:
    $o0 = "dword_411E44" wide ascii nocase
    $o1 = "dword_411E58" wide ascii nocase
    $o2 = "copy_tail_loop" wide ascii nocase
    $o3 = "lpCharType" wide ascii nocase
  condition:
    4 of ($o*)
}