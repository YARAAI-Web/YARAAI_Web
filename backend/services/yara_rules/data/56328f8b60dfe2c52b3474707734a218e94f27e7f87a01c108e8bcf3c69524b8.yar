rule auto_rule_20250726163929_9661 {
  strings:
    $o0 = "dword_41A028" wide ascii nocase
    $o1 = "dword_459AC0" wide ascii nocase
    $o2 = "off_418170" wide ascii nocase
    $o3 = "acmStreamReset" wide ascii nocase
  condition:
    4 of ($o*)
}