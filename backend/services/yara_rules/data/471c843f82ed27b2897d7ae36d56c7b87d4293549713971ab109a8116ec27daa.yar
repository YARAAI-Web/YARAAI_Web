rule auto_rule_20250726194918_9303 {
  strings:
    $o0 = "word_405582" wide ascii nocase
    $o1 = "dword_410BA4" wide ascii nocase
    $o2 = "word_4055BA" wide ascii nocase
    $o3 = "dword_407310" wide ascii nocase
    $o4 = "x40110D" wide ascii nocase
  condition:
    4 of ($o*)
}