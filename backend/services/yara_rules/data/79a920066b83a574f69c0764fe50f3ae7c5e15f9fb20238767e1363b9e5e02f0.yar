rule auto_rule_20250726213513_5289 {
  strings:
    $o0 = "finish_loop" wide ascii nocase
    $o1 = "dword_477234" wide ascii nocase
    $o2 = "off_4764F4" wide ascii nocase
  condition:
    3 of ($o*)
}