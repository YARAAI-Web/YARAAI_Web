rule auto_rule_20250726104354_6340 {
  strings:
    $o0 = "dword_78134" wide ascii nocase
    $o1 = "dword_7831C" wide ascii nocase
    $o2 = "init" wide ascii nocase
  condition:
    3 of ($o*)
}