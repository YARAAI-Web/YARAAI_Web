rule auto_rule_20250727013553_8717 {
  strings:
    $o0 = "rtcStrFromVar" wide ascii nocase
    $o1 = "_vbaOnError" wide ascii nocase
  condition:
    all of them
}