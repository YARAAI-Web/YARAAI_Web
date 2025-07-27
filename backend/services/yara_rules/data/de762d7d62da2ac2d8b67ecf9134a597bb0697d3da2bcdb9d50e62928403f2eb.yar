rule auto_rule_20250726192537_6090 {
  strings:
    $o0 = "dwDesiredAccess" wide ascii nocase
    $o1 = "dword_42429C" wide ascii nocase
  condition:
    all of them
}