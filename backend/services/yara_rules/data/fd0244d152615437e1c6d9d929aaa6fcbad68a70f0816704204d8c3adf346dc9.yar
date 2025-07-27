rule auto_rule_20250727022030_7083 {
  strings:
    $o0 = "x7677u" wide ascii nocase
    $o1 = "xF89C853C" wide ascii nocase
    $o2 = "wvsprintfA" wide ascii nocase
  condition:
    3 of ($o*)
}