import scala.io.Source

object Day02Part1 {
    def checkReport(report: List[Int]): Boolean = {
        var isIncreasing = true
        for (i <- 1 to report.length - 1) {
            if (i == 1) {
                isIncreasing = report(i) > report(i - 1)
            } else if (report(i) > report(i - 1) != isIncreasing) {
                return false
            }
            if (math.abs(report(i) - report(i - 1)) < 1 || math.abs(report(i) - report(i - 1)) > 3) {
                return false
            }
        }
        true
    }
    
    def checkReportTolerate(report: List[Int]): Boolean = {
        for (i <- 0 to report.length - 1) {
            if (checkReport(report.patch(i, Nil, 1))) {
                return true
            }
        }
        false
    }
    
  def main(args: Array[String]) {
    val reports: List[List[Int]] = Source.fromFile("input.txt")
        .getLines()
        .map(line =>
            line.split("\\s+")
                .map(_.toInt)
                .toList
        )
        .toList
        
    var results = 0
    for (report <- reports) {
        if (checkReportTolerate(report)) {
            results += 1
        }
    }
    println(results)
  }
}
