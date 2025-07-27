rule auto_rule_20250726173022_0718 {
  strings:
    $o0 = "dword_44B65C" wide ascii nocase
    $o1 = "off_44B554" wide ascii nocase
  condition:
    all of them
}