rule auto_rule_20250726194519_2389 {
  strings:
    $o0 = "TrailDown1" wide ascii nocase
    $o1 = "_ctype" wide ascii nocase
    $o2 = "main_loop_0" wide ascii nocase
    $o3 = "dword_44A030" wide ascii nocase
    $o4 = "dword_449ACC" wide ascii nocase
  condition:
    4 of ($o*)
}