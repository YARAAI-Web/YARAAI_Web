rule auto_rule_20250726170349_9661 {
  strings:
    $o0 = "byte_40BE12" wide ascii nocase
    $o1 = "ActiveWindow" wide ascii nocase
    $o2 = "tail_loop_start" wide ascii nocase
    $o3 = "word_40BE10" wide ascii nocase
    $o4 = "x1FFFF" wide ascii nocase
  condition:
    4 of ($o*)
}