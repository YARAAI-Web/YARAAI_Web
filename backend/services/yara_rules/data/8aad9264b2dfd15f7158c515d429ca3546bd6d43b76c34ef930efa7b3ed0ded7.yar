rule auto_rule_20250726173932_3342 {
  strings:
    $o0 = "copy_start" wide ascii nocase
    $o1 = "dword_449AB0" wide ascii nocase
  condition:
    all of them
}