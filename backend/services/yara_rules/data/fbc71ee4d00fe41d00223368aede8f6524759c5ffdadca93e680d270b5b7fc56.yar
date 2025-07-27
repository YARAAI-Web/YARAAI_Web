rule auto_rule_20250726100442_6934 {
  strings:
    $o0 = "dword_401A38" wide ascii nocase
    $o1 = "a11sid172bddf8C" wide ascii nocase
    $o2 = "nIDCheckButton" wide ascii nocase
  condition:
    3 of ($o*)
}