rule auto_rule_20250727022835_9633 {
  strings:
    $o0 = "tmMaxCharWidth" wide ascii nocase
    $o1 = "off_426B02" wide ascii nocase
    $o2 = "x1CE4u" wide ascii nocase
  condition:
    3 of ($o*)
}