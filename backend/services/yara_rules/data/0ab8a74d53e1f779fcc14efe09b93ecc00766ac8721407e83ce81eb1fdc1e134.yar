rule auto_rule_20250726123410_9911 {
  strings:
    $o0 = "GetPixel" wide ascii nocase
    $o1 = "byte_456A3C" wide ascii nocase
  condition:
    all of them
}