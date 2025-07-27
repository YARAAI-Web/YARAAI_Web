rule auto_rule_20250726193936_3617 {
  strings:
    $o0 = "a11sid172bddf8C" wide ascii nocase
    $o1 = "nIDButton" wide ascii nocase
    $o2 = "lpDefault" wide ascii nocase
  condition:
    3 of ($o*)
}