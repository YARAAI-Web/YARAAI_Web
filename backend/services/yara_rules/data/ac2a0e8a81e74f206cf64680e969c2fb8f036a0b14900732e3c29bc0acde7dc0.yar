rule auto_rule_20250727011056_2465 {
  strings:
    $o0 = "hObjectb" wide ascii nocase
    $o1 = "ntohl" wide ascii nocase
  condition:
    all of them
}