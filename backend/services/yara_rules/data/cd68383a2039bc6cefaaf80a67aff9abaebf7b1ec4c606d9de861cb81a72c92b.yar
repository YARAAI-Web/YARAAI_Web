rule auto_rule_20250726145154_0509 {
  strings:
    $o0 = "dword_45CF10" wide ascii nocase
    $o1 = "copy_tail_loop" wide ascii nocase
    $o2 = "byte_45CAFC" wide ascii nocase
  condition:
    3 of ($o*)
}