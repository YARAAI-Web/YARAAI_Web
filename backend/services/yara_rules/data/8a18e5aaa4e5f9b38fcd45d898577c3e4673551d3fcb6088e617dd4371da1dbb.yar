rule auto_rule_20250727035154_6101 {
  strings:
    $o0 = "aXklzawercdapqc" wide ascii nocase
  condition:
    all of them
}