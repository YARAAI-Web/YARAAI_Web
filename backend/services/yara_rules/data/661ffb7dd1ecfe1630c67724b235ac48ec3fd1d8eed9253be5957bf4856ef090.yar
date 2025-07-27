rule auto_rule_20250727034213_2425 {
  strings:
    $o0 = "ntohl" wide ascii nocase
    $o1 = "_strlwr" wide ascii nocase
  condition:
    all of them
}