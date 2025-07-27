rule auto_rule_20250726221532_8056 {
  strings:
    $o0 = "tail_loop_start_0" wide ascii nocase
    $o1 = "dword_4770E4" wide ascii nocase
    $o2 = "dword_477230" wide ascii nocase
  condition:
    3 of ($o*)
}